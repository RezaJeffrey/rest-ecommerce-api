import axiosInstance from "../../../api/axiosInstance";

const fetchProducts = () => {
  const controller = new AbortController();
  const res = axiosInstance.get("/products/api/v1/product/", {
    signal: controller.signal,
    transformRequest: (data, headers) => {
      delete headers["Authorization"];
      return data;
    },
  });
  return { res, cancel: () => controller.abort() };
};

export { fetchProducts };
