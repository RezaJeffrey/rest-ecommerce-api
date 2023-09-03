import { useForm } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";
import Navbar from "../../Navbar/Navbar";
import {
  FormControl,
  FormLabel,
  Input,
  FormHelperText,
  Button,
  Box,
  Alert,
} from "@chakra-ui/react";
import {
  signupUser,
  signupSchema,
  singupFormData,
} from "../service/auth_service";
import { useState } from "react";
import { useNavigate } from "react-router-dom";

interface formFieldLevelError {
  username: string[] | null;
  password: string[] | null;
  first_name: string[] | null;
  last_name: string[] | null;
  email: string[] | null;
  phone_number: string[] | null;
  national_code: string[] | null;
  role: string[] | null;
}

function Signup() {
  const [errorMessage, setErrorMessage] = useState<string | null>(null);
  const [fieldErrors, setFieldErrors] = useState<formFieldLevelError>();
  const navigate = useNavigate();
  const {
    register,
    handleSubmit,
    formState: { errors, isValid },
  } = useForm<singupFormData>({
    resolver: zodResolver(signupSchema),
  });
  const roleOptions = [
    {
      id: 1,
      value: "cs",
      label: "customer",
    },
    {
      id: 2,
      value: "sl",
      label: "seller",
    },
  ];
  const handleSignUp = (data: singupFormData) => {
    const res = signupUser(data);
    res
      .then((data) => {
        console.log(data);
        navigate("/users/login/", { replace: true });
      })
      .catch((err) => {
        console.log(err.response?.data);
        setErrorMessage(err.response.data.message);
        setFieldErrors(err.response.data.error);
        console.log(fieldErrors);
      });
  };
  return (
    <>
      <Navbar />
      {errorMessage && <Alert status="error">{errorMessage}</Alert>}
      <form onSubmit={handleSubmit((data) => handleSignUp(data))}>
        <FormControl>
          <FormLabel>username</FormLabel>
          <Input {...register("username")} />
          {errors.username?.message && (
            <FormHelperText>{errors.username.message}</FormHelperText>
          )}
          {fieldErrors?.username &&
            fieldErrors.username.map((err) => (
              <FormHelperText>{err}</FormHelperText>
            ))}
        </FormControl>
        <FormControl>
          <FormLabel>password</FormLabel>
          <Input type="password" {...register("password")} />
          {errors.password?.message && (
            <FormHelperText>{errors.password.message}</FormHelperText>
          )}
          {fieldErrors?.password &&
            fieldErrors.password.map((err) => (
              <FormHelperText>{err}</FormHelperText>
            ))}
        </FormControl>
        <FormControl>
          <FormLabel>first_name</FormLabel>
          <Input {...register("first_name")} />
          {errors.first_name?.message && (
            <FormHelperText>{errors.first_name.message}</FormHelperText>
          )}
          {fieldErrors?.first_name &&
            fieldErrors.first_name.map((err) => (
              <FormHelperText>{err}</FormHelperText>
            ))}
        </FormControl>
        <FormControl>
          <FormLabel>last_name</FormLabel>
          <Input {...register("last_name")} />
          {errors.last_name?.message && (
            <FormHelperText>{errors.last_name.message}</FormHelperText>
          )}
          {fieldErrors?.last_name &&
            fieldErrors.last_name.map((err) => (
              <FormHelperText>{err}</FormHelperText>
            ))}
        </FormControl>
        <FormControl>
          <FormLabel>email</FormLabel>
          <Input {...register("email")} />
          {errors.email?.message && (
            <FormHelperText>{errors.email.message}</FormHelperText>
          )}
          {fieldErrors?.email &&
            fieldErrors.email.map((err) => (
              <FormHelperText>{err}</FormHelperText>
            ))}
        </FormControl>
        <FormControl>
          <FormLabel>phone_number</FormLabel>
          <Input {...register("phone_number", { valueAsNumber: true })} />
          {errors.phone_number?.message && (
            <FormHelperText>{errors.phone_number.message}</FormHelperText>
          )}
          {fieldErrors?.phone_number &&
            fieldErrors.phone_number.map((err) => (
              <FormHelperText>{err}</FormHelperText>
            ))}
        </FormControl>
        <FormControl>
          <FormLabel>national_code</FormLabel>
          <Input {...register("national_code", { valueAsNumber: true })} />
          {errors.national_code?.message && (
            <FormHelperText>{errors.national_code.message}</FormHelperText>
          )}
          {fieldErrors?.national_code &&
            fieldErrors.national_code.map((err) => (
              <FormHelperText>{err}</FormHelperText>
            ))}
        </FormControl>
        <FormControl padding="10px">
          <select {...register("role")}>
            {roleOptions.map((option) => (
              <option value={option.value} key={option.id}>
                {option.label}
              </option>
            ))}
          </select>
          {fieldErrors?.role &&
            fieldErrors.role.map((err) => (
              <FormHelperText>{err}</FormHelperText>
            ))}
        </FormControl>
        <Box display="flex" justifyContent="center" padding="10px">
          <Button type="submit" isDisabled={!isValid} colorScheme="blue">
            Signup
          </Button>
        </Box>
      </form>
    </>
  );
}

export default Signup;
