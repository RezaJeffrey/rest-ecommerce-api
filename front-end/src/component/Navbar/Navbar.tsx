import {
  Box,
  Button,
  Flex,
  HStack,
  useColorMode,
  useColorModeValue,
} from "@chakra-ui/react";
import Logo from "./items/Logo";
import SearchBox from "./items/SearchBox";
import NavButtons from "./items/NavBUttons";

function Navbar() {
  return (
    <Box>
      <Flex
        mb="5"
        borderBottom={2}
        borderStyle={"solid"}
        borderColor={useColorModeValue("gray.900", "whiteAlpha.900")}
        align={"center"}
      >
        <Logo />
        <Flex flex={1} justify={"center"}>
          <SearchBox />
        </Flex>
        <Flex>
          <NavButtons />
        </Flex>
      </Flex>
    </Box>
  );
}

export default Navbar;
