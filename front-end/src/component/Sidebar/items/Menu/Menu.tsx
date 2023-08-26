import { Collapse, Flex, Icon, useDisclosure } from "@chakra-ui/react";
import { ChevronRightIcon, ChevronDownIcon } from "@chakra-ui/icons";
import { ReactNode } from "react";

interface Prob {
  name: string;
  children: ReactNode;
}

function Menu({ name, children }: Prob) {
  const { onToggle, isOpen } = useDisclosure();
  return (
    <>
      <Flex direction="column" as="nav">
        <Flex
          onClick={onToggle}
          fontSize="2xl"
          fontFamily="serif"
          backgroundColor="gray.500"
          padding="10px"
          borderRadius="10px"
          alignItems="center"
          justifyContent="space-between"
          _hover={{
            cursor: "pointer",
            backgroundColor: "gray.600",
          }}
        >
          {name}
          {isOpen ? (
            <Icon as={ChevronDownIcon} />
          ) : (
            <Icon as={ChevronRightIcon} />
          )}
        </Flex>
        <Collapse in={isOpen}>{children}</Collapse>
      </Flex>
    </>
  );
}

export default Menu;
