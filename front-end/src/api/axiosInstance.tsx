import axios from "axios";

export const ACCESS_TOKEN = "ACCESS_TOKEN";
export const REFRESH_TOKEN = "REFRESH_TOKEN";

const axiosInstance = axios.create({
  baseURL: "http://127.0.0.1:8000/",
  timeout: 5000,
  headers: {
    Authorization: `Bearer ${window.localStorage.getItem(ACCESS_TOKEN)}`,
    "Content-Type": "application/json",
  },
});

export default axiosInstance;
