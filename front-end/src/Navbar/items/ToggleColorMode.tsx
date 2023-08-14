import { HStack, Switch, useColorMode } from "@chakra-ui/react";
import { Text } from "@chakra-ui/react";

function ToggleColorMode() {
  const { toggleColorMode, colorMode } = useColorMode();
  return (
    <>
      <HStack>
        <Switch colorScheme="blue" onChange={toggleColorMode} />
        <Text>{colorMode === "dark" ? "ligh" : "dark"} mode </Text>
      </HStack>
    </>
  );
}

export default ToggleColorMode;
