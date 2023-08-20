import axiosInstance from "../../../api/axiosInstance";

const fetchProducts = () => {
  const controller = new AbortController();
  const res = axiosInstance.get("/products/api/v1/product/", {
    signal: controller.signal,
  });
  return { res, cancel: () => controller.abort() };
};

export { fetchProducts };
