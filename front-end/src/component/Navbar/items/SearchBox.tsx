import { SearchIcon } from "@chakra-ui/icons";
import {
  InputGroup,
  InputLeftElement,
  Input,
  Text,
  useOutsideClick,
  VStack,
  List,
  ListItem,
} from "@chakra-ui/react";
import { MutableRefObject, useRef, useState } from "react";

const options = [{ label: "hello" }, { label: "world" }];

function SearchBox() {
  const ref = useRef<HTMLElement>(null);
  const [isListOpen, setIsListOpen] = useState(false);
  useOutsideClick({
    ref: ref,
    handler: () => setIsListOpen(false),
  });
  return (
    <>
      <VStack>
        <InputGroup
          display="flex"
          justifyItems="center"
          size="lg"
          width={1000}
          onClick={() => setIsListOpen(true)}
        >
          <InputLeftElement>
            <SearchIcon />
          </InputLeftElement>
          <Input placeholder="Search Box" borderRadius="16px" />
        </InputGroup>
        {isListOpen && (
          <List spacing={3}>
            {options.map((option, idx) => (
              <ListItem key={idx}>{option.label}</ListItem>
            ))}
          </List>
        )}
      </VStack>
    </>
  );
}

export default SearchBox;
