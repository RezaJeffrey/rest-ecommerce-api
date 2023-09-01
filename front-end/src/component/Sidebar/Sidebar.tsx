import { Stack } from "@chakra-ui/react";
import Categories from "./items/Categories/Categories";
import { categoryEventData } from "../NestedList/NestedList";
import Brands, { BrandOptions } from "./items/Brands/Brands";
import { MultiValue } from "react-select";
import Shops, { ShopOptions } from "./items/Shops/Shops";

interface Prob {
  handleCategory: (e: categoryEventData) => void;
  handleBrand: (e: MultiValue<BrandOptions>) => void;
  handleShop: (e: MultiValue<ShopOptions>) => void;
}

function Sidebar({ handleCategory, handleBrand, handleShop }: Prob) {
  return (
    <>
      <Stack padding={1}>
        <Categories handleCategory={(e) => handleCategory(e)} />
        <Brands handleBrand={(e) => handleBrand(e)} />
        <Shops handleShop={(e) => handleShop(e)} />
      </Stack>
    </>
  );
}

export default Sidebar;
