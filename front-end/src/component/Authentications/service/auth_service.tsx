import axiosInstance, {
  ACCESS_TOKEN,
  REFRESH_TOKEN,
} from "../../../api/axiosInstance";
import { z } from "zod";

export const schema = z.object({
  username: z
    .string({
      invalid_type_error: "username field is required!",
    })
    .min(1),
  password: z
    .string({
      invalid_type_error: "password field is required!",
    })
    .min(1),
});

export type loginFormData = z.infer<typeof schema>;

class AuthService {
  loginUser(data: loginFormData) {
    const res = axiosInstance.post("/users/api/v1/token/", data).then((res) => {
      const access = res.data.access;
      const refresh = res.data.refresh;
      localStorage.setItem(ACCESS_TOKEN, access);
      localStorage.setItem(REFRESH_TOKEN, refresh);
      axiosInstance.defaults.headers.Authorization = `Barear ${window.localStorage.getItem(
        ACCESS_TOKEN
      )}`;
    });
    return res;
  }
}

export default new AuthService();
