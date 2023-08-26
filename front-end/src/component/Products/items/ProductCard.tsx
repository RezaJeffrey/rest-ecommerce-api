import { Card, CardBody, Image, Box, VStack, Text } from "@chakra-ui/react";
import { Product } from "../../../hooks/useProducts";
import noImageAvailable from "../../../assets/noImageAvailable.png";

interface Prob {
  result: Product;
}

function ProductCard({ result }: Prob) {
  return (
    <Card>
      <Box display="flex" justifyContent="center">
        <Image
          src={
            result.images.length
              ? result.images.shift()?.image
              : noImageAvailable
          }
          boxSize="500"
          alt={
            result.images
              ? result.images.shift()?.alt_text
              : "no image is available!"
          }
        />
      </Box>
      <CardBody>
        <VStack>
          <Text>{result.name}</Text>
          <Text>{result.category.name}</Text>
        </VStack>
      </CardBody>
    </Card>
  );
}

export default ProductCard;
