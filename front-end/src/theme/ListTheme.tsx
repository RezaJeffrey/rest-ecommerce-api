import { createMultiStyleConfigHelpers } from "@chakra-ui/react";
import { listAnatomy as parts } from "@chakra-ui/anatomy";
import { mode } from "@chakra-ui/theme-tools";

const { definePartsStyle, defineMultiStyleConfig } =
  createMultiStyleConfigHelpers(parts.keys);

const baseStyle = definePartsStyle((props) => ({
  container: {
    p: 10,
    width: "200%",
    border: "1px",
    borderRadius: "20px",
    listStylePos: "inside", // change listStylePos to inside
    boxShadow: "md", // change boxShadow to md
    mb: "2",
  },
  item: {
    p: 2, // set padding to 2
    border: "1px",
    borderRadius: "20px",
    "&::marker": {
      // change color for marker
      color: mode("green.500", "green.200")(props),
    },
    _hover: {
      color: mode("red.500", "red.300")(props),
      cursor: "pointer",
    },
  },
  icon: {
    //change color for icon
    color: mode("blue.500", "blue.200"),
  },
}));

export const listTheme = defineMultiStyleConfig({ baseStyle });
