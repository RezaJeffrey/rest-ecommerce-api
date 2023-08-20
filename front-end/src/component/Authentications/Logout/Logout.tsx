import { useContext, useEffect, useState } from "react";
import { logoutUser } from "../service/auth_service";
import { Box, Text } from "@chakra-ui/react";
import { userContext } from "../../../context/userContext";
import Navbar from "../../Navbar/Navbar";

function Logout() {
  const [isLogouted, setIsLogouted] = useState(false);
  const { setUser } = useContext(userContext);
  useEffect(() => {
    logoutUser().then(() => {
      setUser({ username: null });
      setIsLogouted(true);
    });
  }, []);
  return (
    <>
      <Navbar />
      {isLogouted ? (
        <Box>
          <Text>logged out successfully!</Text>
        </Box>
      ) : (
        <Box>
          <Text>you should authenticate first to perform this action!</Text>
        </Box>
      )}
    </>
  );
}

export default Logout;
