import { Grid, GridItem, Show } from "@chakra-ui/react";
import Navbar from "./component/Navbar/Navbar";
import ProductsMain from "./component/Products/ProductsMain";
import Sidebar from "./component/Sidebar/Sidebar";
import { useState } from "react";
import { categoryEventData } from "./component/NestedList/NestedList";

function App() {
  const [selectedCategories, setSelectedCategories] = useState<string[]>([]);
  const handleCategory = (e: categoryEventData) => {
    if (e.isChecked) {
      setSelectedCategories([...selectedCategories, e.sku]);
    } else {
      setSelectedCategories(selectedCategories.filter((sku) => sku != e.sku));
    }
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
            />
          </GridItem>
        </Show>
        <GridItem area={"main"}>
          <ProductsMain categories={selectedCategories} />
        </GridItem>
      </Grid>
    </>
  );
}

export default App;
