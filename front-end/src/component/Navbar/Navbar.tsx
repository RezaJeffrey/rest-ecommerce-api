import { Box, Button, HStack } from "@chakra-ui/react";
import Logo from "./items/Logo";
import ToggleColorMode from "./items/ToggleColorMode";
import { useNavigate } from "react-router-dom";
import { ACCESS_TOKEN } from "../../api/axiosInstance";

function Navbar() {
  const navigate = useNavigate();
  return (
    <HStack justifyContent="space-between" padding="10px">
      <Box>
        <Logo />
      </Box>
      <HStack>
        {localStorage.getItem(ACCESS_TOKEN) ? (
          <Button onClick={() => navigate("/users/logout/", { replace: true })}>
            Logout
          </Button>
        ) : (
          <HStack>
            <Button
              onClick={() => navigate("/users/login/", { replace: true })}
            >
              Login
            </Button>
            <Button
              onClick={() => navigate("/users/signup/", { replace: true })}
            >
              Signup
            </Button>
          </HStack>
        )}
        <Button onClick={() => navigate("/", { replace: true })}>Home</Button>
        <ToggleColorMode />
      </HStack>
    </HStack>
  );
}

export default Navbar;
