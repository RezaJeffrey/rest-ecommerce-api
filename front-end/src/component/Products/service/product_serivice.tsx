import axiosInstance from "../../../api/axiosInstance";
import { Product } from "../../../hooks/useProducts";

export interface productFilters {
  name?: string;
  categories?: string[];
  brands?: string[];
  shops?: string[];
  price?: number[];
}

const fetchProducts = ({
  categories = [],
  brands = [],
  shops = [],
  price = [],
  name = "",
}: productFilters) => {
  const paramObj = {
    name: name,
    categories: categories.join(", "),
    brands: brands.join(", "),
    shops: shops.join(", "),
    price: price.join(", "),
  };
  const params = new URLSearchParams(paramObj);
  const controller = new AbortController();
  const res = axiosInstance.get<Product[]>("/products/api/v1/product/", {
    signal: controller.signal,
    params: { params },
    transformRequest: (data, headers) => {
      delete headers["Authorization"];
      return data;
    },
  });
  return { res, cancel: () => controller.abort() };
};

export { fetchProducts };
