import { Stack } from "expo-router";
import "../global.css";

export default function RootLayout() {
    return (
        <Stack screenOptions={{
            statusBarStyle: "light",
            contentStyle: {
                backgroundColor: '#171c1f',
            },
            headerStyle: {
                backgroundColor: '#171c1f',
            },
            headerTintColor: '#fff',
            headerShadowVisible: false,
        }}>
            <Stack.Screen name="(tabs)" options={{ headerShown: false }} />
        </Stack>
    );
}
