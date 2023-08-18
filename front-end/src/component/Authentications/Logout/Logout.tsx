import { useEffect, useState } from "react";
import { logoutUser } from "../service/auth_service";
import { Box, Text } from "@chakra-ui/react";

function Logout() {
  const [isLogouted, setIsLogouted] = useState(false);
  useEffect(() => {
    logoutUser().then(() => {
      setIsLogouted(true);
    });
  }, []);
  return (
    <>
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
