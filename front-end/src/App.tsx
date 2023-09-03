import { Grid, GridItem, Show } from "@chakra-ui/react";
import Navbar from "./component/Navbar/Navbar";
import ProductsMain from "./component/Products/ProductsMain";
import Sidebar from "./component/Sidebar/Sidebar";
import { useState } from "react";
import { categoryEventData } from "./component/NestedList/NestedList";
import { MultiValue } from "react-select";
import { BrandOptions } from "./component/Sidebar/items/Brands/Brands";
import { ShopOptions } from "./component/Sidebar/items/Shops/Shops";

function App() {
  const [selectedCategories, setSelectedCategories] = useState<string[]>([]);
  const [selectedBrands, setSelectedBrands] = useState<string[]>([]);
  const [selectedShops, setSelectedShops] = useState<string[]>([]);
  const [selectedPriceRange, setSelectedPriceRange] = useState<number[]>([]);
  const handleCategory = (e: categoryEventData) => {
    if (e.isChecked) {
      setSelectedCategories([...selectedCategories, e.sku]);
    } else {
      setSelectedCategories(selectedCategories.filter((sku) => sku != e.sku));
    }
  };
  const handleBrand = (e: MultiValue<BrandOptions>) => {
    setSelectedBrands(e.map((brand) => brand.sku));
  };
  const handleShop = (e: MultiValue<ShopOptions>) => {
    setSelectedShops(e.map((shop) => shop.value));
  };
  const handlePrice = (e: number[]) => {
    setSelectedPriceRange([e[0], e[1]]);
  };
  return (
    <>
      <Grid
        templateAreas={{
          base: `"nav" "main"`,
          lg: `"nav nav" "side main"`,
        }}
      >
        <GridItem area={"nav"}>
          <Navbar />
        </GridItem>
        <Show above="lg">
          <GridItem area={"side"}>
            <Sidebar
              handleCategory={(e: categoryEventData) => handleCategory(e)}
              handleBrand={(e: MultiValue<BrandOptions>) => handleBrand(e)}
              handleShop={(e: MultiValue<ShopOptions>) => handleShop(e)}
              handlePrice={(e: number[]) => handlePrice(e)}
            />
          </GridItem>
        </Show>
        <GridItem area={"main"}>
          <ProductsMain
            categories={selectedCategories}
            brands={selectedBrands}
            shops={selectedShops}
            price={selectedPriceRange}
          />
        </GridItem>
      </Grid>
    </>
  );
}

export default App;
