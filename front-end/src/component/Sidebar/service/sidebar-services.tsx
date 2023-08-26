import axiosInstance from "../../../api/axiosInstance";
import { Category } from "../../../hooks/useCategories";

const fetchCategories = () => {
  const controller = new AbortController();
  const res = axiosInstance.get<Category[]>("/categories/api/v1/category/", {
    signal: controller.signal,
    transformRequest: (data, headers) => {
      delete headers["Authorization"];
      return data;
    },
  });
  return { res, cancel: () => controller.abort() };
};
export { fetchCategories };
