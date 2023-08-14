import { HStack } from "@chakra-ui/react";
import Logo from "./items/Logo";
import ToggleColorMode from "./items/ToggleColorMode";

function Navbar() {
  return (
    <HStack justifyContent="space-between" padding="10px">
      <Logo />
      <ToggleColorMode />
    </HStack>
  );
}

export default Navbar;
