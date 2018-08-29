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

  constructor(private characterService: CharacterService) { }

  ngOnInit() {
    this.getCharacters();
  }

  getCharacters(): void {
    this.characterService.getCharacters().subscribe(characters => this.rpg_characters = characters);
  }

  add(name: string): void {
    name = name.trim();
    if(!name) { return; }
    this.characterService.addCharacter({ name } as RPGcharacter).subscribe(character => {this.rpg_characters.push(character)});
  }

  delete(character: RPGcharacter): void {
    this.rpg_characters = this.rpg_characters.filter(h => h !== character);
    this.characterService.deleteCharacter(character).subscribe();
  }
}
