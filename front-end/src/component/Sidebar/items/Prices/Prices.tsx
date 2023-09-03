import {
  Box,
  RangeSlider,
  RangeSliderFilledTrack,
  RangeSliderThumb,
  RangeSliderTrack,
  Text,
  Tooltip,
} from "@chakra-ui/react";
import { useEffect, useState } from "react";
import { fetchMaxPrice } from "../../service/sidebar-services";

interface Prob {
  handlePrice: (e: number[]) => void;
}

export default function Prices({ handlePrice }: Prob) {
  const [errorMessage, setErrorMessage] = useState<string | null>(null);
  const [range, setRange] = useState<number[]>([0, 100]);
  let [maxRange, setMaxRange] = useState<number>();
  const handleEndChange = (e: number[]) => {
    setRange(e);
    handlePrice(e);
  };
  useEffect(() => {
    const { res, cancel } = fetchMaxPrice();

    res
      .then((response) => {
        setMaxRange(response.data.maximum_price);
        setErrorMessage(null);
      })
      .catch((err) => {
        if (err.message) setErrorMessage(err.message);
      });
    return () => cancel();
  }, []);
  return (
    <>
      {errorMessage ? (
        <Text>{errorMessage}</Text>
      ) : (
        <Box padding={10}>
          <Text fontFamily="serif" fontSize="4xl">
            Prices
          </Text>
          <RangeSlider
            aria-label={["min", "max"]}
            defaultValue={[0, 0]}
            min={0}
            max={maxRange}
            width={300}
            height={50}
            size="lg"
            onChangeEnd={(e) => handleEndChange(e)}
          >
            <RangeSliderTrack height={2} borderRadius={10}>
              <RangeSliderFilledTrack />
            </RangeSliderTrack>
            <Tooltip label={range[0]} isOpen>
              <RangeSliderThumb index={0} />
            </Tooltip>
            <Tooltip label={range[1]} isOpen>
              <RangeSliderThumb index={1} />
            </Tooltip>
          </RangeSlider>
        </Box>
      )}
    </>
  );
}
