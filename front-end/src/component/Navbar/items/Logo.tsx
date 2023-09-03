import logo_dark from "../../../assets/default-monochrome-white.svg";
import logo_light from "../../../assets/default-monochrome-black.svg";
import { useColorMode } from "@chakra-ui/react";
import { Image } from "@chakra-ui/react";

function Logo() {
  const { colorMode } = useColorMode();
  return (
    <Image
      src={colorMode === "dark" ? logo_dark : logo_light}
      boxSize="200px"
    />
  );
}

export default Logo;
