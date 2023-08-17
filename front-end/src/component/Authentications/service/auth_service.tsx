import axiosInstance, {
  ACCESS_TOKEN,
  REFRESH_TOKEN,
} from "../../../api/axiosInstance";
import { z } from "zod";

export const loginSchema = z.object({
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

export const signupSchema = z.object({
  username: z.string().min(1, { message: "this field is required!" }),
  password: z.string().min(1, { message: "this field is required!" }),
  first_name: z.string().min(1, { message: "this field is required!" }),
  last_name: z.string().min(1, { message: "this field is required!" }),
  email: z.string().email({ message: "email is not valid!" }),
  phone_number: z.number(),
  national_code: z.number(),
  role: z
    .string({ required_error: "this field is required!" })
    .max(2, { message: "invalid choice entered!" }),
});

export type singupFormData = z.infer<typeof signupSchema>;

export type loginFormData = z.infer<typeof loginSchema>;

const loginUser = (data: loginFormData) => {
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
};

const signupUser = (data: singupFormData) => {
  const res = axiosInstance.post("users/api/v1/register/", data);
  return res;
};
export { loginUser, signupUser };
