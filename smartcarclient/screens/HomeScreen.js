import React from 'react';
import {
  Image,
  Platform,
  ScrollView,
  StyleSheet,
  Text,
  TouchableOpacity,
  View,
  FlatList,
} from 'react-native';

const DUMMY_INVENTORY_DATA = [
  { name: 'tooth brush', id: '1' },
  { name: 'tooth paste', id: '2' },
  { name: 'floss', id: '3' },
  { name: 'baby wipes', id: '4' },
  { name: 'hand sanitizier', id: '5' },
];

export default class HomeScreen extends React.Component {
  static navigationOptions = {
    header: null,
  };

  _keyExtractor = (item, index) => item.id;

  render() {
    return (
      <View style={styles.container}>
        <View style={styles.content_container}>
          <FlatList
            data={DUMMY_INVENTORY_DATA}
            keyExtractor={this._keyExtractor}
            renderItem={({ item }) => <Text>{item.name}</Text>}
          />
          <Text>Hello world</Text>
        </View>
      </View>
    );
  }
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
  },
  content_container: {
    paddingTop: 30,
  },
});
