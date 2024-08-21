```csharp
namespace Project.Application.UseCases.Brands.CreateBrand
{
    public class CreateBrandCommand : ICommand<CreateBrandDto>
    {
        public CreateBrandCommand(
            string id, 
            string organizationId, 
            Guid categoryId, 
            string name, 
            string? title)
        {
            Id = id;
            OrganizationId = organizationId;
            CategoryId = categoryId;
            Name = name;
            Title = title;
        }

        public string Id { get; }
        public string OrganizationId { get; }
        public Guid CategoryId { get; }
        public string Name { get; }
        public string? Title { get; }
    }
}
```