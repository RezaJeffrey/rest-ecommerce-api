import { HStack, Button } from "@chakra-ui/react";
import { ACCESS_TOKEN } from "../../../api/axiosInstance";
import ToggleColorMode from "./ToggleColorMode";
import { useNavigate } from "react-router-dom";

function NavButtons() {
  const navigate = useNavigate();
  return (
    <>
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
    </>
  );
}

export default NavButtons;
