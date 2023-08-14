import { Grid, GridItem, Show } from "@chakra-ui/react";
import Navbar from "./Navbar/Navbar";

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
          <GridItem area={"side"} bgColor="blue">
            side
          </GridItem>
        </Show>
        <GridItem area={"main"} bgColor="orange">
          main
        </GridItem>
      </Grid>
    </>
  );
}

export default App;
