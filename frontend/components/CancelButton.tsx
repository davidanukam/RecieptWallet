import React from "react";
import { Pressable, Text, View } from "react-native";

type Props = {
    label: string;
    icon: React.ReactNode;
    onClick?: () => void;
}

export default function CancelButton({ label, icon, onClick }: Props) {
    return (
        <View className="w-[320px] h-[68px] mx-[20px] my-[20px] items-center p-[3px]">
            <Pressable
                className="flex-row rounded-2xl bg-[#ef4444] shadow-xl w-full h-full items-center justify-center gap-5"
                onPress={onClick}>

                {icon}

                <Text className="text-black text-xl font-medium">
                    {label}
                </Text>
            </Pressable>
        </View>
    )
}
