import { useBrands } from "../../../../hooks/useBrands";
import { Container, FormControl, Text } from "@chakra-ui/react";

import {
  GroupBase,
  MultiValue,
  OptionBase,
  Select,
  SelectComponentsConfig,
  chakraComponents,
  useChakraSelectProps,
} from "chakra-react-select";

export interface BrandOptions extends OptionBase {
  value: string;
  label: string;
  sku: string;
}

const customComponents: SelectComponentsConfig<
  BrandOptions,
  true,
  GroupBase<BrandOptions>
> = {
  Option: ({ children, ...props }) => (
    <chakraComponents.Option {...props}>{children}</chakraComponents.Option>
  ),
  MultiValueContainer: ({ children, ...props }) => (
    <chakraComponents.MultiValueContainer {...props}>
      {children}
    </chakraComponents.MultiValueContainer>
  ),
};

interface Prob {
  handleBrand: (data: MultiValue<BrandOptions>) => void;
}

function Brands({ handleBrand }: Prob) {
  const { brands, error } = useBrands();
  const brandOptions: BrandOptions[] = [];
  brands?.map((brand) =>
    brandOptions.push({
      value: brand.name,
      label: brand.name,
      sku: brand.sku,
    })
  );
  const selectProbs = useChakraSelectProps({
    isMulti: true,
    name: "brands",
    options: brandOptions,
    placeholder: "Select Brands...",
    components: customComponents,
    onChange(newValue) {
      handleBrand(newValue);
    },
  });
  return (
    <>
      {error && <Text>{error}</Text>}
      <Container mb={16}>
        <FormControl p={4}>
          <Text fontFamily="serif" fontSize="4xl">
            Brands
          </Text>
          <Select {...selectProbs} />
        </FormControl>
      </Container>
    </>
  );
}

export default Brands;
