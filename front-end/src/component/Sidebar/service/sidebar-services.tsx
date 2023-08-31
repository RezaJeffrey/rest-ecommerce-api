import axiosInstance from "../../../api/axiosInstance";

const fetchSideBarItems = <T,>(endpoint: string) => {
  const controller = new AbortController();
  const res = axiosInstance.get<T[]>(endpoint, {
    signal: controller.signal,
    transformRequest: (data, headers) => {
      delete headers["Authorization"];
      return data;
    },
  });
  return { res, cancel: () => controller.abort() };
};

export { fetchSideBarItems };
