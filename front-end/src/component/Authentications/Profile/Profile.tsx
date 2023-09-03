import { useEffect, useState } from "react";
import { getUserProfile, refreshToken } from "../service/auth_service";
import Navbar from "../../Navbar/Navbar";
import { Box, Button, Text } from "@chakra-ui/react";
import { useNavigate } from "react-router-dom";

interface User {
  username: string;
  first_name: string;
  last_name: string;
}

function Profile() {
  const [user, setUser] = useState<User>();
  const [isAuth, setIsAuth] = useState(false);
  const [repeat, setRepeat] = useState(0);
  const navigate = useNavigate();
  useEffect(() => {
    const { res, cancel } = getUserProfile();
    res
      .then((data) => {
        setUser(data.data.profile);
        setIsAuth(true);
      })
      .catch((err) => {
        if (err.response.status === 401 && !repeat) {
          refreshToken();
          setRepeat(1);
        } else {
          setIsAuth(false);
        }
      });
    return () => cancel();
  }, [repeat]);
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
