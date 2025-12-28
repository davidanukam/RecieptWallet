import { Alert, Pressable, Text, View } from "react-native";

type Props = {
    label: string;
    onClick?: () => void;
}

export default function UploadButton({ label, onClick }: Props) {
    return (
        <View className="w-[320px] h-[68px] mx-[20px] my-[20px] items-center p-[3px]">
            <Pressable
                className="rounded-[10px] w-full h-full items-center content-center flex-1"
                onPress={onClick}>
                <Text className="bg-[#155DFC] p-5 rounded-xl text-white">{label}</Text>
            </Pressable>
        </View>
    )
}
