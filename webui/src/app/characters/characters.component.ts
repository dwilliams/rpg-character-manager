import { Component, OnInit } from '@angular/core';
import { RPGcharacter } from '../rpgcharacter';
import { RPGCHARACTERS } from '../mock-rpgcharacters';

@Component({
  selector: 'app-characters',
  templateUrl: './characters.component.html',
  styleUrls: ['./characters.component.css']
})
export class CharactersComponent implements OnInit {
  rpg_characters = RPGCHARACTERS;

  selectedCharacter: RPGcharacter;

  constructor() { }

  ngOnInit() {
  }

  onSelect(character: RPGcharacter): void {
    this.selectedCharacter = character;
  }

}
