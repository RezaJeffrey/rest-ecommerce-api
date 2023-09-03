import { useState } from "react";
import axiosInstance from "../../../api/axiosInstance";

interface MaxPrice {
  maximum_price: number;
}

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

const fetchMaxPrice = () => {
  const controller = new AbortController();
  const res = axiosInstance.get<MaxPrice>(
    "/products/api/v1/product/get_maximum_price/",
    {
      signal: controller.signal,
      transformRequest: (data, headers) => {
        delete headers["Authorization"];
        return data;
      },
    }
  );

  return { res, cancel: () => controller.abort() };
};

export { fetchSideBarItems, fetchMaxPrice };
