import { Grid, GridItem, Show } from "@chakra-ui/react";
import Navbar from "./component/Navbar/Navbar";
import ProductsMain from "./component/Products/ProductsMain";
import Sidebar from "./component/Sidebar/Sidebar";

function App() {
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
            <Sidebar />
          </GridItem>
        </Show>
        <GridItem area={"main"}>
          <ProductsMain />
        </GridItem>
      </Grid>
    </>
  );
}

export default App;
