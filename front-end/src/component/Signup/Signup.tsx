import { useForm } from "react-hook-form";
import { z } from "zod";
import { zodResolver } from "@hookform/resolvers/zod";
import Navbar from "../Navbar/Navbar";
import {
  FormControl,
  FormLabel,
  Input,
  FormHelperText,
  Button,
  Box,
} from "@chakra-ui/react";

const schema = z.object({
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

type formDate = z.infer<typeof schema>;

function Signup() {
  const {
    register,
    handleSubmit,
    formState: { errors, isValid },
  } = useForm<formDate>({
    resolver: zodResolver(schema),
  });
  const roleOptions = [
    {
      value: "cs",
      label: "customer",
    },
    {
      value: "sl",
      label: "seller",
    },
  ];
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
          <Input {...register("password")} />
          {errors.password?.message && (
            <FormHelperText>{errors.password.message}</FormHelperText>
          )}
        </FormControl>
        <FormControl>
          <FormLabel>first_name</FormLabel>
          <Input {...register("first_name")} />
          {errors.first_name?.message && (
            <FormHelperText>{errors.first_name.message}</FormHelperText>
          )}
        </FormControl>
        <FormControl>
          <FormLabel>last_name</FormLabel>
          <Input {...register("last_name")} />
          {errors.last_name?.message && (
            <FormHelperText>{errors.last_name.message}</FormHelperText>
          )}
        </FormControl>
        <FormControl>
          <FormLabel>email</FormLabel>
          <Input {...register("email")} />
          {errors.email?.message && (
            <FormHelperText>{errors.email.message}</FormHelperText>
          )}
        </FormControl>
        <FormControl>
          <FormLabel>phone_number</FormLabel>
          <Input {...register("phone_number", { valueAsNumber: true })} />
          {errors.phone_number?.message && (
            <FormHelperText>{errors.phone_number.message}</FormHelperText>
          )}
        </FormControl>
        <FormControl>
          <FormLabel>national_code</FormLabel>
          <Input {...register("national_code", { valueAsNumber: true })} />
          {errors.national_code?.message && (
            <FormHelperText>{errors.national_code.message}</FormHelperText>
          )}
        </FormControl>
        <FormControl padding="10px">
          <select {...register("role")}>
            {roleOptions.map((option) => (
              <option value={option.value}>{option.label}</option>
            ))}
          </select>
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
