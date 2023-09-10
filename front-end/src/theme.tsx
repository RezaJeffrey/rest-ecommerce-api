import { ThemeConfig, extendTheme } from "@chakra-ui/react";
import { listTheme } from "./theme/ListTheme";

const config: ThemeConfig = {
  initialColorMode: "light",
};

const theme = extendTheme({ config, components: { List: listTheme } });

export default theme;
