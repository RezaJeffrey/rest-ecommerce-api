import { useEffect, useState } from "react";
import { getUserProfile } from "../service/auth_service";
import { AxiosResponse } from "axios";
import Navbar from "../../Navbar/Navbar";
import { Box, Button, Text } from "@chakra-ui/react";
import { Navigate, useNavigate } from "react-router-dom";

interface User {
  username: string;
  first_name: string;
  last_name: string;
}

function Profile() {
  const [user, setUser] = useState<User>();
  const [isAuth, setIsAuth] = useState(false);
  const navigate = useNavigate();
  useEffect(() => {
    const { res, cancel } = getUserProfile();
    res
      .then((data) => {
        setUser(data.data.profile);
        setIsAuth(true);
        console.log(data.data.profile);
      })
      .catch((err) => {
        setIsAuth(false);
        console.log(err);
      });
    return () => cancel();
  }, []);
  const handleClick = () => {
    navigate("/users/login/", { replace: true });
  };
  return (
    <>
      <Navbar />
      <Box>
        {isAuth ? (
          <div>
            <Text>username: {user?.username}</Text>
            <Text>first name: {user?.first_name}</Text>
            <Text>last name: {user?.last_name}</Text>
          </div>
        ) : (
          <div>
            <Text>your not authenticated!</Text>
            <Box padding="10px" display="flex" justifyContent="center">
              <Button onClick={handleClick} colorScheme="blue">
                Go To Login
              </Button>
            </Box>
          </div>
        )}
      </Box>
    </>
  );
}

export default Profile;
