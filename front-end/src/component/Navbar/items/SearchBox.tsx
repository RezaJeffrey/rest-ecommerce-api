import { SearchIcon } from "@chakra-ui/icons";
import {
  InputGroup,
  InputLeftElement,
  Input,
  useOutsideClick,
  VStack,
  List,
  ListItem,
  Box,
} from "@chakra-ui/react";
import { ChangeEvent, useRef, useState } from "react";
import { useProducts } from "../../../hooks/useProducts";

function SearchBox() {
  const ref = useRef<HTMLDivElement>(null);
  const [isListOpen, setIsListOpen] = useState(false);
  const [name, setName] = useState("");
  const handleChange = (e: ChangeEvent<HTMLInputElement>) => {
    e.preventDefault();
    setName(e.target.value);
  };
  useOutsideClick({
    ref: ref,
    handler: () => setIsListOpen(false),
  });
  const { products } = useProducts({ name: name }, [name]);

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
          <Input
            placeholder="Search Box"
            borderRadius="16px"
            onChange={(e) => handleChange(e)}
          />
        </InputGroup>
        {isListOpen && (
          <Box display="flex" justifyContent="center" width="100%" ref={ref}>
            <List spacing={3}>
              {products.map((product, idx) => (
                <ListItem key={idx}>{product.name}</ListItem>
              ))}
            </List>
          </Box>
        )}
      </VStack>
    </>
  );
}

export default SearchBox;
