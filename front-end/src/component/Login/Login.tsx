import {
  Box,
  Button,
  FormControl,
  FormHelperText,
  FormLabel,
  Input,
} from "@chakra-ui/react";
import { useForm } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";
import { z } from "zod";
import Navbar from "../Navbar/Navbar";

const schema = z.object({
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

type formData = z.infer<typeof schema>;

function Login() {
  const {
    register,
    handleSubmit,
    formState: { errors, isValid },
  } = useForm<formData>({ resolver: zodResolver(schema) });
  return (
    <>
      <Navbar />
      <form onSubmit={handleSubmit((data) => console.log(data))}>
        <FormControl>
          <FormLabel>username</FormLabel>
          <Input {...register("username")} />
          {errors.username?.message && (
            <FormHelperText>{errors.username.message}</FormHelperText>
          )}
        </FormControl>
        <FormControl>
          <FormLabel>password</FormLabel>
          <Input type="password" {...register("password")} />
          {errors.password?.message && (
            <FormHelperText>{errors.password.message}</FormHelperText>
          )}
        </FormControl>
        <Box display="flex" justifyContent="center" padding="10px">
          <Button type="submit" isDisabled={!isValid} colorScheme="blue">
            Login
          </Button>
        </Box>
      </form>
    </>
  );
}

export default Login;
