import axiosInstance from "../../../api/axiosInstance";
import { Product } from "../../../hooks/useProducts";

export interface productFilters {
  categories: string[];
}

const fetchProducts = ({ categories }: productFilters) => {
  console.log(categories);
  const paramObj = {
    categories: categories.join(", "),
    prices: "13, 14, 15",
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
  res.then(() => {
    console.log(params);
  });
  return { res, cancel: () => controller.abort() };
};

export { fetchProducts };
