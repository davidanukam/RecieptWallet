import { Image } from "expo-image";
import { cssInterop } from "nativewind";

cssInterop(Image, {
    className: "style",
});

type Props = {
    imgSource: string;
};

export default function ImageViewer({ imgSource }: Props) {
    return (
        <Image
            source={imgSource}
            className="w-[320px] h-[440px] rounded-[18px] shadow-md"
        />
    );
}
