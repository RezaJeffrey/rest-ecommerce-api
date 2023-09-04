import { SearchIcon } from "@chakra-ui/icons";
import { Input, InputGroup, InputLeftElement, Stack } from "@chakra-ui/react";

function SearchBox() {
  return (
    <>
      <Stack spacing={3}>
        <InputGroup width="400%">
          <InputLeftElement>
            <SearchIcon />
          </InputLeftElement>
          <Input placeholder="Search Box" />
        </InputGroup>
      </Stack>
    </>
  );
}

export default SearchBox;
