import { Stack } from "expo-router";
import { Text, View } from "react-native";

export default function EditScreen() {
    return (
        <View className="flex-1 items-center justify-center bg-[#171c1f]">
            <Stack.Screen options={{ title: 'Edit Receipt' }} />
            <Text className="my-5 text-white">Edit Image</Text>
        </View>
    );
}
