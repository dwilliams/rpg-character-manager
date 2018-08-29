import { Component, OnInit } from '@angular/core';
import { RPGcharacter } from '../rpgcharacter';
import { CharacterService } from '../character.service';

@Component({
  selector: 'app-characters',
  templateUrl: './characters.component.html',
  styleUrls: ['./characters.component.css']
})
export class CharactersComponent implements OnInit {
  rpg_characters: RPGcharacter[];

  selectedCharacter: RPGcharacter;

  constructor(private characterService: CharacterService) { }

  ngOnInit() {
    this.getCharacters();
  }

  onSelect(character: RPGcharacter): void {
    this.selectedCharacter = character;
  }

  getCharacters(): void {
    this.characterService.getCharacters().subscribe(characters => this.rpg_characters = characters);
  }
}
