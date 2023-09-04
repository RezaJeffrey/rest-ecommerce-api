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
        <Flex flex={1} ml={-2} display={"flex"}>
          <Logo />
        </Flex>
        <Flex flex={1} justify={"start"} mr="400">
          <SearchBox />
        </Flex>
        <Flex ml="400">
          <NavButtons />
        </Flex>
      </Flex>
    </Box>
  );
}

export default Navbar;
