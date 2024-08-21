```
// Declaração da entidade com especificação do nome no plural
entity Brand (Brands) {
	id: string // Se não for informado -> id: uuid
	categoryId: uuid
	name: string
	title: string? // opcional
}

// Declaração dos relacionamentos
Brand.organization -< Organization.brands // one to many
Brand.localizations >- BrandLocalization.brand // many to one
Brand.users >< User.brands // many to many
Brand.categoryId -> Category.id // left to right
```