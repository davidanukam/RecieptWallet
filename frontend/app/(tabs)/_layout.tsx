import Feather from '@expo/vector-icons/Feather';
import FontAwesome5 from '@expo/vector-icons/FontAwesome5';
import { Tabs } from 'expo-router';

export default function TabLayout() {
    return (
        <Tabs screenOptions={{
            tabBarActiveTintColor: '#32CD32',
        }}>
            <Tabs.Screen name="index" options={{
                title: 'Home',
                tabBarIcon: ({ color, focused }) => (
                    <FontAwesome5 name="home" size={24} color="black" />
                ),
            }} />
            <Tabs.Screen name="upload" options={{
                title: 'Upload',
                tabBarIcon: ({ color, focused }) => (
                    <Feather name="upload" size={24} color="black" />
                ),
            }} />
        </Tabs>
    );
}
