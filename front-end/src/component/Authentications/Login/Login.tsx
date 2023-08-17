import {
  Alert,
  Box,
  Button,
  FormControl,
  FormHelperText,
  FormLabel,
  Input,
} from "@chakra-ui/react";
import { useForm } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";
import Navbar from "../../Navbar/Navbar";
import { useState } from "react";
import AuthService, { schema, loginFormData } from "../service/auth_service";

function Login() {
  const [errorMessage, setErrorMessage] = useState<string | null>(null);
  const {
    register,
    handleSubmit,
    formState: { errors, isValid },
  } = useForm<loginFormData>({ resolver: zodResolver(schema) });
  const handleLogin = (data: loginFormData) => {
    const res = AuthService.loginUser(data);
    res
      .then(() => {
        setErrorMessage(null);
      })
      .catch((err) => {
        setErrorMessage(err.response.data.detail);
        console.log(errorMessage);
      });
  };
  return (
    <>
      <Navbar />
      {errorMessage && <Alert status="error">{errorMessage}</Alert>}
      <form onSubmit={handleSubmit((data) => handleLogin(data))}>
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
