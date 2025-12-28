import Feather from '@expo/vector-icons/Feather';
import FontAwesome5 from '@expo/vector-icons/FontAwesome5';
import { Tabs } from 'expo-router';

export default function TabLayout() {
    return (
        <Tabs screenOptions={{
            tabBarActiveTintColor: '#8bd0ef',
            tabBarInactiveTintColor: '#888',
            tabBarStyle: {
                backgroundColor: '#171c1f',
                borderTopColor: '#171c1f',
            },
            headerStyle: {
                backgroundColor: '#171c1f',
                borderBottomColor: '171c1f',
            },
            headerTintColor: '#fff',
        }}>
            <Tabs.Screen name="index" options={{
                title: 'Home',
                tabBarIcon: ({ color }) => (
                    <FontAwesome5 name="home" size={24} color={color} />
                ),
            }} />
            <Tabs.Screen name="upload" options={{
                title: 'Upload',
                tabBarIcon: ({ color }) => (
                    <Feather name="upload" size={24} color={color} />
                ),
            }} />
        </Tabs>
    );
}
