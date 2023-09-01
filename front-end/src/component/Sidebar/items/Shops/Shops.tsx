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
import { useShop } from "../../../../hooks/useShops";

export interface ShopOptions extends OptionBase {
  value: string;
  label: string;
}

const customComponents: SelectComponentsConfig<
  ShopOptions,
  true,
  GroupBase<ShopOptions>
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
  handleShop: (data: MultiValue<ShopOptions>) => void;
}

function Shops({ handleShop }: Prob) {
  const { shops, errorMessage } = useShop();
  const shopOtions: ShopOptions[] = [];
  shops.map((shop) => {
    shopOtions.push({
      value: shop.sku,
      label: shop.name,
    });
  });
  const selectProbs = useChakraSelectProps({
    isMulti: true,
    name: "shops",
    options: shopOtions,
    placeholder: "Select Shops...",
    components: customComponents,
    onChange(newValue) {
      handleShop(newValue);
    },
  });
  return (
    <>
      {errorMessage && <Text>{errorMessage}</Text>}
      <Container mb={16}>
        <FormControl p={4}>
          <Text fontFamily="serif" fontSize="4xl">
            Shops
          </Text>
          <Select {...selectProbs} />
        </FormControl>
      </Container>
    </>
  );
}

export default Shops;
