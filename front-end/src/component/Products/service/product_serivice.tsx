import axiosInstance from "../../../api/axiosInstance";
import { Product } from "../../../hooks/useProducts";
import Brands from "../../Sidebar/items/Brands/Brands";

export interface productFilters {
  categories: string[];
  brands: string[];
}

const fetchProducts = ({ categories, brands }: productFilters) => {
  const paramObj = {
    categories: categories.join(", "),
    brands: brands.join(", "),
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
