import axiosInstance from "../../../api/axiosInstance";
import { Product } from "../../../hooks/useProducts";

export interface productFilters {
  categories: string[];
  brands: string[];
  shops: string[];
}

const fetchProducts = ({ categories, brands, shops }: productFilters) => {
  const paramObj = {
    categories: categories.join(", "),
    brands: brands.join(", "),
    shops: shops.join(", "),
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
